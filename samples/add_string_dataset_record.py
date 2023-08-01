"""
This sample creates a dataset comprising string records
if one does not exist and adds a record to the dataset.
The sample demonstrates the higher order C2 dataset and string record abstractions
that hide the details of object and record creation and hashing.
This example builds on the create_set.py code and omits redundant comments.
"""

import pprint

from c2 import (
    C2,
    Web3HTTPCommitmentService,
    C2StringSeries,
)


DATASET_NAME = "TestDataset"


"""
C2 initialization
"""

c2 = C2(Web3HTTPCommitmentService(**Web3HTTPCommitmentService.get_dotenv_init_args()))

"""
C2 operations
"""

ds = C2StringSeries(c2, DATASET_NAME)

# Add a record to the dataset.
# The caller must retain this data to verify the commitment record
# at a later time.
receipt = ds.add_record(record="TestRecord")
print("c2ds.add_record() receipt: ")
pprint.pprint(receipt)

assert ds.verify_commitments()
