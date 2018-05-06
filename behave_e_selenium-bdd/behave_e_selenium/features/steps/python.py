from behave import given, then

@given('que o usuario acesso a pagina "{link}"')
def acessar_link(context, link):
    context.browser.get(link)

@then('a mensagem "{msg}" devera estar no titulo')
def checa_titulo(context, msg):
    assert context.browser.title == msg

@given('que usuario inputou "{msg}" e submeteu formulario')
def input(context, msg):
    context.browser.find_element_by_id('id-search-field').send_keys(msg)
    context.browser.find_element_by_id('submit').click()

@then('redirecionado para pagina de "{rst}"')
def checa_titulo(context, rst):
    assert context.browser.find_element_by_xpath('//*[@id="content"]/div/section/form/h3').text == rst
