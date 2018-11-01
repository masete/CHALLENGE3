signup_schema = {
    'user_name':{'required': True, 'min':6, 'type':'string'},
    'email':{'required':True, 'min':12, 'type':'string','regex':'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
    'password':{'required':True, 'min':8, 'type':'integer'}
}

login_schema = {
    'user_name':{'type':'string'},
    'password':{'required': True, 'min':8, 'max':12}
}
post_product_schema = {
    'product_name':{'required': True,'type':'string'},
    'product_price':{'required': True,'type':'integer'},
}

modify_product_schema = {
    'product_name':{'required': True,'type':'string'},
    'product_price':{'required': True,'type':'integer'}

}

post_sale_schema = {
    'sale_quantity':{'required': True,'type':'integer'},
    'sale_price':{'required': True,'type':'integer'}

}
delete_product_schema = {
    'product_name':{'required': True,'type':'string'},
    'product_price':{'required': True,'type':'integer'}

}
get_product_schema = {
    'product_name':{'required': True,'type':'string'},
    'product_price':{'required': True,'type':'integer'}

}
get_sale_schema = {
    'sale_quantity':{'required': True,'type':'integer'},
    'sale_price':{'required': True,'type':'integer'}


}