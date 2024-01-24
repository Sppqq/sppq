from g4f import ChatCompletion, get_model_and_provider, Provider
import g4f

def str_to_class(classname):
    if classname == 'g4f.models.gpt_35_turbo':
        return g4f.models.gpt_35_turbo
    elif classname == 'g4f.models.gpt_4':
        return g4f.models.gpt_4

def ask_gpt(prompt:str, model='g4f.models.gpt_35_turbo', stream=None)->str:

    # Specify the provider manually
    provider = Provider.DeepInfra

    # Set the arguments for get_model_and_provider
    ignored = None
    # Include both "model" and "provider" arguments
    model, _ = get_model_and_provider(provider=provider, stream=stream, ignored=ignored, model=str_to_class(model))

    # Create the ChatCompletion object
    response = ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response