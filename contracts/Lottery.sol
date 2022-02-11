// SPDX-License-Identifier: MIT

pragma solidity ^0.8.10;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    AggregatorV3Interface internal priceFeed;

    address[] public players;
    uint256 public usdEntreeFee;

    constructor(address _priceFeedAddress) {
        usdEntreeFee = 50 * (10**18);
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function enter() public payable {
        // Minimum $50
        require(msg.value >= getEntranceFee());
        players.push(msg.sender);
    }

    function getEntranceFee() public view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        // Multiply with 10**10 to make it equivanlent of 18 decimals
        uint256 adjustedPrice = uint256(price) * 10**10;
        uint256 entranceFee = (usdEntreeFee * 10**18) / (adjustedPrice);
        return entranceFee;
    }

    function startLottery() public {}

    function endLottery() public {}
}
