# coding: utf-8


class SMSKingErrorResponse(Exception):
    """
    未知錯誤
    """

    def __init__(self, url, status_code, response):
        self.url = url
        self.status_code = status_code
        self.response = response

    def __str__(self):
        return 'SMSKingErrorResponse({0}, {1}, response={2})'.format(self.url, self.status_code, self.response)


class SMSKingErrorCodeResponse(SMSKingErrorResponse):
    """
    已知錯誤，帶有錯誤代碼
    """

    def __init__(self, url, status_code, response, error_code):
        super(SMSKingErrorCodeResponse, self).__init__(url, status_code, response)

        self.error_code = error_code

    def __str__(self):
        return 'SMSKingErrorCodeResponse({0}, {1}, response={2}, error_code={3})'.format(self.url, self.status_code, self.response, self.error_code)
