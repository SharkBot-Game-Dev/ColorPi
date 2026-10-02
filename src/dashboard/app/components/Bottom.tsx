'use client'

function Bottom() {
  return (
    <div>
        <header className="flex justify-between p-3 text-left bg-[var(--bg-menu)]">
            <div className="grid grid-cols-1 sm:grid-cols-5 gap-4">
                <a href="/"><div className="p-1 text-white text-center">
                    <div className="flex">
                        <img src="/avatar.png" className="h-[40px] w-[65px] pl-5" />
                        <h3 className="pl-5 pt-3">ColorPi</h3>
                    </div><br/>
                    <p>
                        Copyright © 2026<br/>
                        ColorPi All rights reserved.
                    </p>
                </div></a>
                <div className="p-1 text-white text-center">
                    <h3 className="pt-3">製品</h3><hr/>
                    <p>
                        <a href="/products/bot">多機能Bot (ColorPi)</a>
                    </p>
                </div>
                <div className="p-1 text-white text-center">
                    <h3 className="pt-3">パートナー様</h3><hr/>
                    <p>
                        <a href="https://www.sharkbot.xyz/">SharkBot</a>
                    </p>
                </div>
                <div className="p-1 text-white text-center">
                    <h3 className="pt-3">SNSなど</h3><hr/>
                    <p>
                        <a href="https://github.com/ColorPi-Dev">Github</a>
                    </p>
                </div>
            </div>
        </header>
    </div>
  )
}

export default Bottom
