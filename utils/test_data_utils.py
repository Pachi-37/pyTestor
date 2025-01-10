class TestInfo:
    def __init__(self, data_list):
        self.id = data_list[0]
        self.title = data_list[1]
        self.module = data_list[2]
        self.url = data_list[3]
        self.request_type = data_list[4]
        self.need_login = data_list[5]
        self.input_data = data_list[6]
        self.data_type = data_list[7]
        self.expect_result = data_list[8]
        self.response_code = None
