import base64
import codecs

# function that returns base64 representation of a string
def get_b64(string):
    message = string
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

# void function that returns nothing, but writes some string content into a file
def write_to_file(string):
    file = codecs.open("txt.txt", "w", "utf-8")
    file.write(string)
    file.close()


message = "Python is fun"
# assign function result to a "message" variable
message = get_b64(message)
write_to_file(message)

