def setup():

    from .qt_widget import GAIAScatterWidget
    from glue.config import qt_client

    qt_client.add(GAIAScatterWidget)
