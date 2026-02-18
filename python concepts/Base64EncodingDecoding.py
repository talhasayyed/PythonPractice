# program to encode and decode using base64 encription

import base64
data = "abc123!?$*&()'-=@~"

print("Actual String data is = ",data)

# Standard Base64 Encoding
encodedBytes = base64.b64encode(data.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print("encoded is = ",encodedStr)

# Base64 decription
decodedBytes = base64.b64decode(encodedStr.encode("utf-8"))
decodedStr = str(decodedBytes, "utf-8")

print("decoded is = ",decodedBytes)
