// frontend/src/components/header/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import Dropdown from './dropdown'

const rootElement = document.getElementById('dropdown-root')
const dropdownTitle = rootElement.getAttribute('data-title')

ReactDOM.render(<Dropdown title={dropdownTitle} />, rootElement);
