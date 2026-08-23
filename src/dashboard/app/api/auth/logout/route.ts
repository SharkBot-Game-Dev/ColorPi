import { NextRequest, NextResponse } from "next/server";
import { auth } from "@/lib/auth";

export async function GET(request: NextRequest) {
    const result = await auth.api.signOut({ headers: request.headers, asResponse: true });
    const response = NextResponse.redirect(new URL("/", "https://color.sharkbot.jp"));
    for (const cookie of result.headers.getSetCookie()) {
        response.headers.append("set-cookie", cookie);
    }
    return response;
}