from page_objects import PageObject, PageElement

class Google(PageObject):

    lstib   = PageElement(id_='lst-ib')
    btnK    = PageElement(name='btnK')

    def search(self, txt):
        self.lstib.send_keys(txt)
        self.btnK.click()

