# what data type of key , which datatype of value
country_code = {"india":"+91",
                "USA":"+1",
                "Canada":"+1",
                "Australia":"+66"   ,
                "India":"+91"
                }
# allow value as dublicate ,not key
print(country_code)
val=country_code.values()
print(val,type(val))
key=country_code.keys()
print(key)