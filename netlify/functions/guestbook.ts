import type { Config } from "@netlify/functions";
import { desc } from "drizzle-orm";
import { db } from "../../db/index.js";
import { guestbookEntries } from "../../db/schema.js";

const MAX_NAME = 60;
const MAX_MESSAGE = 280;

export default async (req: Request) => {
  if (req.method === "GET") {
    const entries = await db
      .select()
      .from(guestbookEntries)
      .orderBy(desc(guestbookEntries.createdAt))
      .limit(50);
    return Response.json(entries);
  }

  if (req.method === "POST") {
    let body: { name?: unknown; message?: unknown; website?: unknown };
    try {
      body = await req.json();
    } catch {
      return Response.json({ error: "Invalid request." }, { status: 400 });
    }

    // Honeypot: real visitors never see or fill this field.
    if (typeof body.website === "string" && body.website.length > 0) {
      return Response.json({ ok: true }, { status: 201 });
    }

    const name = typeof body.name === "string" ? body.name.trim() : "";
    const message = typeof body.message === "string" ? body.message.trim() : "";

    if (!name || !message) {
      return Response.json({ error: "Please add your name and a message." }, { status: 400 });
    }
    if (name.length > MAX_NAME || message.length > MAX_MESSAGE) {
      return Response.json(
        { error: `Keep names under ${MAX_NAME} and messages under ${MAX_MESSAGE} characters.` },
        { status: 400 },
      );
    }

    const [entry] = await db.insert(guestbookEntries).values({ name, message }).returning();
    return Response.json(entry, { status: 201 });
  }

  return new Response("Method not allowed", { status: 405 });
};

export const config: Config = {
  path: "/api/guestbook",
};
