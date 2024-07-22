import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

function Toggle() {
  const [isOn, toggleOnOff] = useState(true);

  function handleClick() {
    toggleOnOff(!isOn);
  }
  
  return (
    <button onClick={handleClick}>{ isOn ? "ON" : "OFF" }</button>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<Toggle />);
