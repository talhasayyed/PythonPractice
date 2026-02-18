# ENV = "prod"
ENV = "dev"

def mock_data_decorator(func):
    def wrapper(*args, **kwargs):
        if ENV == "dev":
            print("mock mode → skipping actual function call")
            return {"status": "success", "data": "mock response"}  # dummy data
        else:
            return func(*args, **kwargs) # actual function call
    return wrapper


@mock_data_decorator
def normal_function(param1, param2):
    print("calling function -> normal_function()")
    print(f"user input {param1}, {param2}")
    return {"status": "success", "data": "actual function response"}


if __name__ == "__main__":
    print(f"ENV is {ENV}")
    response = normal_function('a', 'b')
    print(f"function return: {response}")
