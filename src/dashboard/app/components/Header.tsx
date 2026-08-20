'use client'

import { useEffect, useRef, useState } from 'react'

function Header() {
  const [isMenuOpen, setMenuOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  function openMenu() {
    if (isMenuOpen) {
        setMenuOpen(false);
    } else {
        setMenuOpen(true);
    }
  }

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setMenuOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <div>
        <header className="flex justify-between pt-5 pr-5 text-left">
            <div className="flex pt-5 text-left">
                <img src="/avatar.png" className="h-[50px] w-[75px] pl-5" />
                <h3 className="pl-5 pt-3">ColorPi</h3>
            </div>
            <button className="my-5 text-right bg-[var(--bg-menu)] p-3 rounded-[30px]" onClick={openMenu}>☰</button>
        </header>

        {isMenuOpen ? <div className="absolute right-0 z-10 text-right" ref={menuRef}>
            <div
            className="
                m-5
                rounded-[30px]
                bg-[var(--bg-menu)]
                p-5
                text-[var(--text-menu)]
            "
            >
                <a
                    href="/"
                    className="m-5 text-[var(--text-menu)] no-underline"
                >
                    ホーム
                </a><br/><br/>
                <a href='https://discord.com/oauth2/authorize?client_id=1537996178157871154' className="m-5 text-[var(--text-menu)] no-underline">Discordに追加</a><br/><br/>
                <a href='https://discord.gg/w58JAwWn5n' className="m-5 text-[var(--text-menu)] no-underline">サポートサーバー</a><br/><br/>
                <a href='https://www.sharkbot.xyz' className="m-5 text-[var(--text-menu)] no-underline">SharkBot</a>
            </div>
        </div> : <div></div>}
    </div>
  )
}

export default Header
