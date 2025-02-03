// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract LimitedToken is ERC20 {
    uint256 public maxSupply = 1_000_000 * 10**18; // 1 млн токенів

    constructor() ERC20("LimitedToken", "LMT") {
        _mint(msg.sender, maxSupply);
    }
}
