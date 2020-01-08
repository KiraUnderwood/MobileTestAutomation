class FillCapabilities(dict):
    """
    Class representing checked dict with capabilities and defining
    if this set of capabilities is fir native or Web apps
    """

    def __init__(self, **kwargs):
        dict.__init__(self, **kwargs)
        self.__dict__ = self.check_required()

    def check_required(self):
        if self.get('platformName') is None or (self.get('deviceName') is None and self.get('udid') is None):
            raise Exception('Min required capabilities are not passed')
        if self.get('app') is not None and self.get('browserName') is not None:
            if self['app'] != '' and self['browserName'] != '':
                raise Exception('Capabilities should be either for Native or for Web App')
        if self.get('browserName') is not None:
            if (self.get('browserName') == 'Chrome' and self['platformName'] == 'iOS') or (
                    self.get('browserName') == 'Safari' and self['platformName'] == 'Android'):
                raise Exception('Browser does not match the device platform type')
        return self

    def is_native(self):
        return self.get('app') is not None and self.get('app') != ''

    def is_web(self):
        return self.get('browserName') is not None and self.get('app') != ''
