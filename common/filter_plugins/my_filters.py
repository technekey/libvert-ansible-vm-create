from ansible.utils.display import Display

class FilterModule(object):
    def filters(self):
        return {
                'warn_user': self.warn_filter
               }

    def warn_filter(self, message, **kwargs):
        Display().warning(message)
