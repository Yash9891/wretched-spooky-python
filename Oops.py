# class Dog:
#     def __init__(self,name, breed):
#         self.name=name
#         self.breed=breed

# class Cat:
#    def  __init(self, name, color):
#         self.name=name 
#         self.color=color

# jerry=Dog(name="Jerry",breed="labordor")
# soli=Dog(name="Soli",breed="labordorin")
# print(jerry.name, jerry.breed)
# print(soli.name, soli.breed)



#Realworld API-------------------------------------------------
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000
