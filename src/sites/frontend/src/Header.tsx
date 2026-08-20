import { useState } from 'react'
import avatarLogo from './assets/avatar.png'
import './App.css'

function Header() {
  const [isMenuOpen, setMenuOpen] = useState(false);

  function openMenu() {
    if (isMenuOpen) {
        setMenuOpen(false);
    } else {
        setMenuOpen(true);
    }
  }

  return (
    <div>
        <div className='header'>
            <div className='headerLogo'>
                <img src={avatarLogo} />
                <h3>ColorPi</h3>
            </div>
            <button onClick={openMenu}>☰</button>
        </div>

        {isMenuOpen ? <div className='headermenu'>
            <div className='box'>
                <a href='https://discord.com/oauth2/authorize?client_id=1537996178157871154'>Discordに追加</a><br/><br/>
                <a href='https://discord.gg/w58JAwWn5n'>サポートサーバー</a>
            </div>
        </div> : <div></div>}
    </div>
  )
}

export default Header
