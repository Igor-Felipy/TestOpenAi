from openai import OpenAI

OpenAI.api_key = "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"

prompt = "Write a haiku about recursion in programming."

response = OpenAI.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.4,
    max_token=64
)

print(response)