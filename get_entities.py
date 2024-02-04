from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You will be provided with 11 hypotheses. "+
                                  "These hypotheses are necessary for development of ontology 'Invasive Biology'." +
                                  "Your task is to distinguish entities from this text"},
    {"role": "user", "content": "The absence of enemies in the exotic range is a cause of invasion success." +
                                "An ecosystem with high biodiversity is more resistant against non-native species than an ecosystem with lower biodiversity." + 
                                "After having been released from natural enemies, non-native species will allocate more energy in growth and/or"+
                                " reproduction (this re-allocation is due to genetic changes), which makes them more competitive." + 
                                "After having been released from natural specialist enemies, non-native species will allocate more energy in cheap (energy-inexpensive)"+
                                " defenses against generalist enemies and less energy in expensive defenses against specialist enemies (this re-allocation is due to genetic changes); the energy gained in "+ 
                                "this way will be invested in growth and/or reproduction, which makes the non-native species more competitive."+
                                "Invasive species are more phenotypically plastic than non-invasive or native ones."+
                                "The invasion success of non-native species is higher in areas that are poor in closely "+
                                "related species than in areas that are rich in closely related species."+
                                "Non-native species are more likely to become established and have major ecological impacts on islands than on continents."+
                                "The invasion success of non-native species is high if they strongly differ from native species, and it is low if they are similar to native species."+
                                "A high propagule pressure (a composite measure consisting of the number of individuals introduced per introduction event and the frequency of introduction events) is a cause of invasion success."+
                                "The invasion success of non-native species is higher in highly disturbed than in relatively undisturbed ecosystems." +
                                "The presence of non-native species in an ecosystem facilitates invasion by additional species, increasing their likelihood of survival or ecological impact."}
  ]
)

print(completion.choices[0].message)