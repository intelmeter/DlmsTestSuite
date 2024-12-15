Feature: IC 01
  As a user I want to be able to read and validate data in IC 01 objects

  Scenario Outline: OBIS-Get
    Given the meter is connected over serial port
    When "<obis>" is read
    Then actual value matches with "<expected value>"

    Examples:
    | obis               | expected value |
    | 0.0.96.1.0.255:2   | AS0000001      |
    | 0.0.42.0.0.255:2   | GRX1           |