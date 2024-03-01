from rocrate.rocrate import ROCrate
import os
import json
from rocrate.model.person import Person

#input data
input_data = {
    "@context": "https://w3id.org/ro/crate/1.1/context",
    "@graph": [
        {
            "@id": "arcp://name,farms-to-freeways-example-dataset",
            "@type": "Dataset",
            "datePublished": "2024-01-31T04:46:07+00:00"
            
        },
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": {
                "@id": "arcp://name,farms-to-freeways-example-dataset"
            },
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            }
        },
        
        {
            "@id": "https://orcid.org/0000-0000-0000-0000",
            "@type": "Person",
            "affiliation": "University of Flatland",
            "name": "Alice Doe"
        },
        {
            "@id": "https://orcid.org/0000-0000-0000-0001",
            "@type": "Person",
            "affiliation": "University of Flatland",
            "name": "Bob Doe"
        }
    ]
}

os.mkdir("input_crate")

with open('input_crate/ro-crate-metadata.json', 'w') as f:
    json.dump(input_data, f)

crate = ROCrate("input_crate")

alice_id = "https://orcid.org/0000-0000-0000-0000"
bob_id = "https://orcid.org/0000-0000-0000-0001"
alice = crate.add(Person(crate, alice_id, properties={
    "name": "Alice Doe",
    "affiliation": "University of Flatland"
}))
bob = crate.add(Person(crate, bob_id, properties={
    "name": "Bob Doe",
    "affiliation": "University of Flatland"
}))

crate.write("exp_crate")
