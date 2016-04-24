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
        return 'SMSKingErrorResponse(response={0})'.format(self.response)


class SMSKingErrorCodeResponse(SMSKingErrorResponse):
    """
    已知錯誤，帶有錯誤代碼
    """

    def __init__(self, url, status_code, response, error_code):
        super(SMSKingErrorCodeResponse, self).__init__(url, status_code, response)

        self.error_code = error_code

    def __str__(self):
        return 'SMSKingErrorCodeResponse(response={0}, error_code={1})'.format(self.response, self.error_code)
