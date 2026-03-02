# CSCE 479 - Homework #2
### Overview
In this assignment you will perform a conceptual design of a P2P system that acts as a secure storage for files. (You are
not going to do the actual implementation for HW2.) This is an open-ended problem with lots of potential for fun
solutions. As such, there are many possible solutions that may meet the outlined requirements.

The goal of the P2P storage infrastructure is for you to be able to store a file on a remote system while preserving the
confidentiality and integrity of the file.

The software tool will allow each machine to operate as a servant (either/both a client or a server).

### Requirements
Client role requirements: This is the machine with the original data.
* When sending the file to the server:
  * Ensure that the file (plaintext) is only visible to the client.
  * Ensure that file can later be tested for integrity.
  * Send the file to the sever and wait for confirmation.
    * File must be encrypted for obvious reasons.
  * Delete the file from local storage (after receiving confirmation).
* When retrieving the file from the server:
  * Confirm integrity of the file after retrieval from server
  * Alert the server upon receipt and verification of the file

Server role requirements: This is the machine where the data will be stored.
* Upon receiving a file (for storage):
  * Ensure that the integrity of the file is preserved while both in transit, and while being stored on the server (itself).
  * Send confirmation to the client
* Upon receiving retrieval request for the file:
  * Confirm that the requester has the necessary credentials to make the request
  * Ensure that the integrity of the file is intact and send the file
  * Get confirmation of the receipt of the file
  * Delete the file from local storage after receipt confirmation is received

The server should NEVER see the original data/plaintext, and must have no clue what it is storing.

You should start by thinking about the various conceptual pieces of the problem including authentication, integrity
checks, confidentiality, etc.

Use illustrations (figures/diagrams/drawings) to describe the protocol rather than using just words. Each scenario
(storing and retrieving) should be described in step by step detail. Use illustrations.

You should start by thinking about how the server and client systems know each other. For this work, you may assume the
use of either (1) a shared secret (key) between the two systems or (2) a set of public-keys through which the systems know
each other; either method can be assumed to have been established out-of-band.
