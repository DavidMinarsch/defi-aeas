import {
  Box,
  Button,
  Center,
  Divider,
  Flex,
  Heading,
  Progress,
  Stat,
  StatArrow,
  StatLabel,
  StatNumber,
  Table,
  Tbody,
  Td,
  Text,
  Th,
  Thead,
  Tr,
} from '@chakra-ui/react'
import * as React from 'react'
import { useWallet } from 'use-wallet'
import { ColorModeSwitcher } from './ColorModeSwitcher'
import Wallet from './components/Wallet'

export const App = () => {
  const wallet = useWallet()

  return (
    <Box vh="100">
      {wallet.status === 'connected' ? (
        <>
          <Flex
            p={6}
            alignItems="center"
            justifyContent="space-between"
            borderBottomWidth={1}
          >
            <Heading size="sm">Placeholder Name</Heading>
            <Flex>
              <Wallet />
              <ColorModeSwitcher />
            </Flex>
          </Flex>
          <Box p={6}>
            <Flex alignItems="center" justifyContent="space-between" mb={7}>
              <Heading>My Uniswap Agent</Heading>
              <Flex>
                <Button mr={3}>Top Up</Button>
                <Button>Withdraw</Button>
                <Center mx={3}>
                  <Divider orientation="vertical" />
                </Center>
                <Button>Settings</Button>
              </Flex>
            </Flex>
            <Flex mb={7}>
              <Stat>
                <Box mb={3}>
                  <StatLabel>Balance</StatLabel>
                  <StatNumber fontSize="4xl">$12,040.00</StatNumber>
                </Box>
              </Stat>
              <Stat>
                <StatLabel>Profit and Loss</StatLabel>
                <Flex alignItems="center">
                  <StatNumber fontStyle="heading" fontSize="4xl" mr={3}>
                    $2,040.00
                  </StatNumber>
                  <StatArrow type="increase" />
                </Flex>
              </Stat>
              <Stat>
                <StatLabel>Agent Health</StatLabel>
                <StatNumber fontSize="4xl">Running</StatNumber>
              </Stat>
            </Flex>
            <Box mb={7}>
              <Heading size="sm" mb={3}>
                Current Allocation
              </Heading>
              <Table m={0}>
                <Thead>
                  <Tr>
                    <Th>Position</Th>
                    <Th>Allocation</Th>
                  </Tr>
                </Thead>
                <Tbody>
                  <Tr>
                    <Td>FET-ETH</Td>
                    <Td>
                      <Flex alignItems="center">
                        <Progress
                          borderRadius={4}
                          value={67}
                          mr={3}
                          width={50}
                        />
                        67%
                      </Flex>
                    </Td>
                  </Tr>
                  <Tr>
                    <Td>ETH</Td>
                    <Td>
                      <Flex alignItems="center">
                        <Progress
                          borderRadius={4}
                          value={33}
                          mr={3}
                          width={50}
                        />
                        33%
                      </Flex>
                    </Td>
                  </Tr>
                </Tbody>
              </Table>
            </Box>
            <Box mb={7}>
              <Heading size="sm" mb={3}>
                Transactions
              </Heading>
              <Table m={0}>
                <Thead>
                  <Tr>
                    <Th>Description</Th>
                    <Th>Amount</Th>
                    <Th>Currency</Th>
                    <Th>Date/Time</Th>
                    <Th>From</Th>
                    <Th>To</Th>
                  </Tr>
                </Thead>
                <Tbody>
                  <Tr>
                    <Td>Agent traded ETH for FET</Td>
                    <Td>8</Td>
                    <Td>ETH</Td>
                    <Td>10:25 28 Jan '21</Td>
                    <Td>0x2DN8...29s4</Td>
                    <Td>0x2DN8...29s4</Td>
                  </Tr>
                  <Tr>
                    <Td>Agent traded ETH for FET</Td>
                    <Td>8</Td>
                    <Td>ETH</Td>
                    <Td>10:25 28 Jan '21</Td>
                    <Td>0x2DN8...29s4</Td>
                    <Td>0x2DN8...29s4</Td>
                  </Tr>
                </Tbody>
              </Table>
            </Box>
          </Box>
        </>
      ) : (
        <Center height="100vh">
          <Box textAlign="center">
            <Heading mb={3}>Placeholder Name</Heading>
            <Text mb={7}>Bit of info 'bout why dis is siiiick</Text>
            <Wallet />
          </Box>
        </Center>
      )}
    </Box>
  )
}
