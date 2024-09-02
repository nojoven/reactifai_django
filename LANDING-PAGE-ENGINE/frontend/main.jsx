import React from 'react'
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'

createRoot(document.getElementById('tiny')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
