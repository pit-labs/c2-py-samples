"""
This sample creates a dataset comprising private integer records
if one does not exist and adds a record to the dataset.
The sample demonstrates the higher order C2 dataset abstraction
that hides the details of object hashing.
This example builds on the create_set.py code and omits redundant comments.
"""

import pprint

from c2 import (
    C2,
    Web3HTTPCommitmentService,
    C2PrivateIntSeries,
)


DATASET_NAME = "TestDataset"

"""
C2 initialization
"""

c2 = C2(Web3HTTPCommitmentService(**Web3HTTPCommitmentService.get_dotenv_init_args()))

"""
C2 operations
"""

# Create the C2 dataset object.
# This will create a new dataset with the given name if one does not exist.
ds = C2PrivateIntSeries(c2, DATASET_NAME)

# Add a record to the dataset.
# The caller must retain this data to verify the commitment record
# at a later time.
receipt = ds.add_record(record=(1, "Salt"))
print("c2ds.add_record() receipt: ")
pprint.pprint(receipt)

assert ds.verify_commitments()
