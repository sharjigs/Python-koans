class Proxy:
    def __init__(self, target_object):
        # print(target_object, '<---')

        #initialize '_obj' attribute last. Trust me on this!
        self._obj = target_object
        print(self._obj)

    def message(self):
        return self._obj.message
  
    # def demo_jigs(self):
    #      string = "pecks.xlx\n"    \
    #             + "orders1.xls\n" \
    #             + "apec1.xls\n"   \
    #             + "na1.xls\n"     \
    #             + "na2.xls\n"     \
    #             + "sa1.xls"

    #     change_this_search_string = 'a..xlx'
    #     self.assertEquals(
    #         len(re.findall(change_this_search_string, string)),
    #         3)

class Television:
    def __init__(self):
        self._channel = None
        self._power = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        if self._power == 'on':
            self._power = 'off'
        else:
            self._power = 'on'

    def is_on(self):
        return self._power == 'on'


tv = Proxy(Television())
# tv.channel = 10
# tv._obj.power()
# print(tv.channel)
# print(tv._obj.is_on())



# tv._obj.power()
# tv.channel = 10

# message = ['power', 'channel']
# print(message)
# print(tv._obj.messages())