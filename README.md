# Ethereum_JHUISI_2019
Security research concerning smart contracts using Solidity and Ethereum.  JHUISI 2019.

/contracts      Solidity contracts used during research.
* Re-entrancy
    - EtherStore.sol
    - Attack.sol
    
/py_geth        Python scripts used for automating the blockchain process.
* genesis.py
    - Creates basic genesis.json file used for blockchain initialization.  Takes some command-line arguments.

Wiki's To Write:
* Solidity / Ethereum Overview

* Solidity Attacks
    - Re-entrancy
    
* References 
Solidity Documentation: https://solidity.readthedocs.io/en/latest/installing-solidity.html#prerequisites-all-operating-systems
Ethereum Development Tutorial: https://github.com/ethereum/wiki/wiki/Ethereum-Development-Tutorial
sigp/solidity-security-blog: https://github.com/sigp/solidity-security-blog#re-vuln
Setting up private network or local cluster: https://github.com/ethereum/go-ethereum/wiki/Setting-up-private-network-or-local-cluster
Understanding smart contract compilation and deployment: https://kauri.io/article/973c5f54c4434bb1b0160cff8c695369/understanding-smart-contract-compilation-and-deployment
Here's how I built a private blockchain...: https://hackernoon.com/heres-how-i-built-a-private-blockchain-network-and-you-can-too-62ca7db556c0
Prototyping a Blockchain Smart Contract: https://medium.com/@chakrvyuh/prototyping-a-blockchain-smart-contract-78877464e38e
