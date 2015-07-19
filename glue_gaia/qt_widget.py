# A scatter widget that automatically updates the data

import numpy as np

from glue.qt.widgets.scatter_widget import ScatterWidget
from glue.core import Data, Component
from glue.core.message import ComponentsChangedMessage

from glue.core.callback_property import add_callback

N = 1e7
X = np.random.uniform(-180., 180, N)
Y = np.random.uniform(-90., 90, N)

def get_data_subset(xmin, xmax, ymin, ymax):
    keep = (X > xmin) & (X < xmax) & (Y > ymin) & (Y < ymax)
    print("Extracting {0} data points".format(np.sum(keep)))
    return X[keep], Y[keep]

class GAIAScatterWidget(ScatterWidget):

    LABEL = "GAIA explorer"

    def __init__(self, session, parent=None):

        super(GAIAScatterWidget, self).__init__(session, parent=parent)

        x, y = get_data_subset(-1., 1., -1., 1.)

        self.gaia_data = Data(label="GAIA")
        self.gaia_data.add_component(x, label='x')
        self.gaia_data.add_component(y, label='y')

        self.session.data_collection.append(self.gaia_data)

        self.add_data(self.gaia_data)

        add_callback(self.client, 'xmin', self.limits_changed)
        add_callback(self.client, 'xmax', self.limits_changed)
        add_callback(self.client, 'ymin', self.limits_changed)
        add_callback(self.client, 'ymax', self.limits_changed)

    def limits_changed(self, *args, **kwargs):

        x, y = get_data_subset(self.client.xmin, self.client.xmax, self.client.ymin, self.client.ymax)

        # Find link between component names and IDs
        component_ids = {}
        for component_id in self.gaia_data._components:
            component_ids[component_id.label] = component_id

        # Remove world and pixel components
        self.gaia_data._components.pop(component_ids['World 0'])
        self.gaia_data._components.pop(component_ids['Pixel Axis 0'])

        # Replace data in components
        xc = Component(x)
        yc = Component(y)
        self.gaia_data._components[component_ids['x']] = xc
        self.gaia_data._components[component_ids['y']] = yc
        self.gaia_data._shape = xc.shape
        self.gaia_data._create_pixel_and_world_components()

        self.client.artists[0].force_update()

