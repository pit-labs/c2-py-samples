"""
C2 dataset creation sample
"""

from dotenv import dotenv_values

from c2 import (
    C2,
    Web3HTTPCommitmentService,
)

# Load environment variables containing C2 configuration.
env_vars = dotenv_values(".env")

# Create a C2 object using a Web3 HTTP commitment service.
# The commitment service is a smart contract running on a blockchain.
# Use connection parameters specified in environment variables.
c2 = C2(
    Web3HTTPCommitmentService(
        # RPC endpoint used to access the blockchain running the
        # commitment service smart contract.
        endpoint_url=env_vars["ENDPOINT_URL"],
        # Address of the smart contract providing the commitment service.
        c2c_address=env_vars["C2C_ADDRESS"],
        # Private key used to access the commitment service.
        # The private key defines the user address that owns the commitments
        # and the corresponding C2 datasets and records.
        private_key=env_vars["PRIVATE_KEY"],
        # This setting should be set for the appropriate chain
        # and is configured in the .env file.
        inject_geth_poa_middleware=env_vars["INJECT_GETH_POA_MIDDLEWARE"],
    )
)

# Create the test dataset commitment.
# This operation records that the user with the above PRIVATE_KEY
# has created the below named dataset.
# Such commitments are used to validate completeness of a collection of user datasets
# and mitigates Sybil attacks (https://en.wikipedia.org/wiki/Sybil_attack).
# Dataset creation is idempotent.
c2.create_dataset("TestDataset")
