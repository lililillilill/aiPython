citys = ["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
new_list=[citys for citys in citys if citys.startswith('s')]
print(new_list)