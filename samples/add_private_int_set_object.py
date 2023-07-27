"""
This sample creates a set comprising private integer objects
if one does not exist and adds a record to the dataset.
This illustrates low-level C2 set and object operations.
Low-level operations expose all C2 features and provide the most control.
This example builds on the create_set.py code and omits redundant comments.
"""

from dotenv import dotenv_values
import pprint

from c2 import C2, Web3HTTPCommitmentService, C2PrivateIntSeries


DATASET_NAME = "TestDataset"

env_vars = dotenv_values(".env")

c2 = C2(
    Web3HTTPCommitmentService(
        endpoint_url=env_vars["ENDPOINT_URL"],
        c2c_address=env_vars["C2C_ADDRESS"],
        private_key=env_vars["PRIVATE_KEY"],
        inject_geth_poa_middleware=bool(env_vars["INJECT_GETH_POA_MIDDLEWARE"]),
    )
)

# Check if the set exists for the current user.
# Dataset creation is idempotent, but it is more efficient
# to create a dataset only if needed.
# The default user is the user initialized with the private_key above.
if not c2.user_named_set_exists(c2.get_default_user(), DATASET_NAME):
    receipt = c2.add_named_set(DATASET_NAME)
    print("add_named_set() receipt: ")
    pprint.pprint(receipt)

# Validate the set commitment.
assert c2.user_named_set_exists(c2.get_default_user(), DATASET_NAME)

# Add a private integer record object for the set.
# Get object hash for the integer record.
object_hash = C2PrivateIntSeries.get_object_hash_for_dataset_record(
    # Name of the set receiving the record object.
    DATASET_NAME,
    # Record object for the private integer series comprises the
    # record value and the salt -- a random string -- that provides randomness
    # and make it impossible to derive the value from the signature.
    (1, "Salt"),
)

# Post the object commitment.
# Since we are merely adding a record to a dataset,
# we just need to create a writable dataset
# that receives the new record commitment.
receipt = c2.add_set_object(
    set_hash=c2.get_named_set_hash(DATASET_NAME),
    object_hash=object_hash,
)
print("add_set_object() receipt: ")
pprint.pprint(receipt)

# Validate the record commitment.
assert c2.verify_user_object(
    user=receipt["user"],
    object_hash=receipt["objectHash"],
    timestamp=receipt["timestamp"],
)
