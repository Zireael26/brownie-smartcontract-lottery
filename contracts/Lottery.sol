// SPDX-License-Identifier: MIT

pragma solidity ^0.8.10;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Lottery is Ownable {
    AggregatorV3Interface internal priceFeed;
    enum LOTTERY_STATE {
        OPEN,
        CLOSED,
        CALCULATING_WINNER
    }

    LOTTERY_STATE public lotteryState;
    address[] public players;
    uint256 public usdEntreeFee;

    constructor(address _priceFeedAddress) {
        usdEntreeFee = 50 * (10**18);
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        lotteryState = LOTTERY_STATE.CLOSED;
    }

    function enter() public payable {
        // Minimum $50
        require(lotteryState == LOTTERY_STATE.OPEN, "Lottery is not open!");
        require(msg.value >= getEntranceFee(), "Not enough ETH!!!");
        players.push(msg.sender);
    }

    function getEntranceFee() public view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        // Multiply with 10**10 to make it equivanlent of 18 decimals
        uint256 adjustedPrice = uint256(price) * 10**10;
        uint256 entranceFee = (usdEntreeFee * 10**18) / (adjustedPrice);
        return entranceFee;
    }

    function startLottery() public onlyOwner {
        require(
            lotteryState == LOTTERY_STATE.CLOSED,
            "Can't start a new lottery while an existing lottery is open!"
        );
        lotteryState = LOTTERY_STATE.OPEN;
    }

    function endLottery() public onlyOwner {
        // uint256 winnerIndex = uint256(
        //     keccak256(
        //         abi.encodePacked(
        //             nonce, // predictable
        //             msg.sender, // predictable
        //             block.difficulty, // can be manipulated by miners
        //             block.timestamp // predictable
        //         )
        //     )
        // ) % players.length;
        //
        // require(
        //     lotteryState == LOTTERY_STATE.OPEN,
        //     "Can't close a lottery that is not open!"
        // );
        // lotteryState = LOTTERY_STATE.CLOSED;
        //
    }
}
