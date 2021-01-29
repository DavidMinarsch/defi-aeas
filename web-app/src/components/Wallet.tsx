import { Box, Button, Text } from '@chakra-ui/react'
import React from 'react'
import { useWallet } from 'use-wallet'

function Wallet() {
  const wallet = useWallet()

  return (
    <>
      {wallet.status === 'connected' ? (
        <Box textAlign="right">
          {/* <Text>Account: {wallet.account}</Text>
          <Text>Balance: {wallet.balance} ETH</Text> */}
          <Button onClick={() => wallet.reset()}>Disconnect</Button>
        </Box>
      ) : (
        <Box>
          <Button onClick={() => wallet.connect('injected')}>
            Connect MetaMask
          </Button>
        </Box>
      )}
    </>
  )
}

export default Wallet
