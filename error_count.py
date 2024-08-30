import language_tool_python

tool = language_tool_python.LanguageTool('en-US')
tool = language_tool_python.LanguageToolPublicAPI('en-us')
org = 'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'

def error_count(message):
    message_split = message.split()
    ans = tool.correct(message)
    ans_split = ans.split()
    errors = 0
    
    for i in range(0,len(ans_split)):
        if message_split[i] != ans_split[i]:
            errors +=1
    return errors

print(error_count(org))