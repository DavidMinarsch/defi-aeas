import { ChakraProvider, ColorModeScript } from '@chakra-ui/react'
import * as React from 'react'
import ReactDOM from 'react-dom'
import { UseWalletProvider } from 'use-wallet'
import { App } from './App'
import theme from './theme'

ReactDOM.render(
  <React.StrictMode>
    <ColorModeScript />
    <UseWalletProvider chainId={1} connectors={{ injected: {} }}>
      <ChakraProvider theme={theme}>
        <App />
      </ChakraProvider>
    </UseWalletProvider>
  </React.StrictMode>,
  document.getElementById('root')
)
