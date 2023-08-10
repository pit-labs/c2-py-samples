"""
This sample creates a C2 set.
A set is a collection of objects.
A named set of data records is a dataset.
Such datasets can implement any point-in-time (PIT) or bitemporal data.
The sample illustrates low-level C2 set operations.
Low-level set operations expose all C2 features and provide the most control.
"""

import pprint

from c2 import (
    C2,
    Web3HTTPCommitmentService,
)


# Name for the test set to create.
DATASET_NAME = "TestDataset"


"""
C2 initialization
"""

# Create a C2 object using a Web3 HTTP commitment service.
# The commitment service is a smart contract running on a blockchain.
# Use connection parameters specified in environment variables.
c2 = C2(Web3HTTPCommitmentService(**Web3HTTPCommitmentService.get_dotenv_init_args()))

"""
C2 operations
"""

# Create the test set commitment.
# This operation records that the user with the above PRIVATE_KEY
# has created the below named dataset.
# Such commitments are used to validate completeness of a collection of user datasets
# and mitigates Sybil attacks (https://en.wikipedia.org/wiki/Sybil_attack).
# Set creation is idempotent.
# Multiple creations will log multiple events, but a single set commitment will be recorded.
receipt = c2.add_named_set(DATASET_NAME)
# The returned receipt contains information on the set commitment.
# It can be optionally retained to simplify subsequent validation.
# All receipts are also available via C2 indexing services.
# Since add_set() calls are idempotent,
# duplicate calls will be noops and will return an empty receipt.
print("add_named_set() receipt: ")
pprint.pprint(receipt)

# Validate the set commitment.
assert c2.user_named_set_exists(c2.get_default_user(), DATASET_NAME)
