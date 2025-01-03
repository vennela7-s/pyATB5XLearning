class APIRestfulBooker:
    name = None
    list_of_apis = []
    set_of_links = {}

    def __init__(self, name, list_of_apis, set_of_links):
        self.name = name
        self.list_of_apis = list_of_apis
        self.set_of_links = set_of_links

    def api_list(self):
        print(f"List of APIs is {self.list_of_apis}")

    def links_set(self):
        print(f"Set of Links is {self.set_of_links}")


print_api_links = APIRestfulBooker("API1", ['Intellexer', 'API2Cart', 'Delion.lo'],
                                {"www.astrology.com", "www.animation.com", "www.avator.com"})
print_api_links.api_list()
print_api_links.links_set()
