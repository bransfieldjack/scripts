{
"Source": "order_notification@thaonguyenpharmacy.com.au",
"ToAddresses": ["bransfieldjack@gmail.com"],
"TemplateName": "thao_nguyen_pharmacy_notifications_template",
"TemplateData": "{\"name\":\"test\",\"lastName\":\"test\", \"email\":\"bransfieldjack@gmail.com\", \"address\":\"ireland\", \"city\":\"ireland\", \"address\":\"ireland\", \"clickandcollect\":\"true\", \"phone\":\"123456\", \"items\":[{\"name\":\"Deep heat\", \"price\":\"$99.99\", \"quantity\":\"4\", \"promotion\":\"$59.99\"}], \"total\":\"$100.00\"}"
}


{
    \"name\":\"test\",
    \"lastName\":\"test\", 
    \"email\":\"bransfieldjack@gmail.com\", 
    \"address\":\"ireland\", 
    \"city\":\"ireland\", 
    \"address\":\"ireland\", 
    \"clickandcollect\":\"true\", 
    \"phone\":\"123456\", 
    \"items\":[
        {
            \"name\":\"Deep heat\", 
            \"price\":\"$99.99\", 
            \"quantity\":\"4\", 
            \"promotion\":\"$59.99\"
        }
    ], 
    \"total\":\"$100.00\"}



    name: "test",
    lastName: "test",
    email: orders[0].Email,
    address: orders[0].address,
    city: orders[0].city,
    address: orders[0].address,
    clickandcollect: orders[0].clickAndCollect,
    phone: orders[0].Phone,
    items: orders[0].Items
    total: orders[0].Total,

    phone: orders[0].Phone,
    clickandcollect: orders[0].clickAndCollect,
    address: orders[0].address,
    postalCode: orders[0].postalCode,
    city: orders[0].city,
    country: orders[0].country,
    postalCode: orders[0].postalCode,
    total: orders[0].Total,
    items: orders[0].Items