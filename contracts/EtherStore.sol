pragma solidity ^0.4.25;
// EtherStore contract pulled from sigp/solidity-security-blog GitHub
// for research purposes.
// https://github.com/sigp/solidity-security-blog.git

contract EtherStore {

  uint256 public withdrawalLimit = 1 ether;
  mapping(address => uint256) public lastWithdrawTime;
  mapping(address => uint256) public balances;

  function depositFunds() public payable {
    balances[msg.sender] += msg.value;

  }

  function withdrawFunds (uint256 _weiToWithdraw) public {
    require(balances[msg.sender] >= _weiToWithdraw);
    // limit the withdrawal
    require(_weiToWithdraw <= withdrawalLimit);
    // limit the time allowed to withdraw
    require(now >= lastWithdrawTime[msg.sender] + 1 weeks);
    require(msg.sender.call.value(_weiToWithdraw)());
    balances[msg.sender] -= _weiToWithdraw;
    lastWithdrawTime[msg.sender] = now;
  }
}
