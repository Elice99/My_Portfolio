import type { Config } from "@netlify/functions";
import { eq, sql } from "drizzle-orm";
import { db } from "../../db/index.js";
import { pageViews } from "../../db/schema.js";

const SITE_KEY = "__site__";

export default async (req: Request) => {
  if (req.method === "POST") {
    const [row] = await db
      .insert(pageViews)
      .values({ path: SITE_KEY, count: 1 })
      .onConflictDoUpdate({ target: pageViews.path, set: { count: sql`${pageViews.count} + 1` } })
      .returning();
    return Response.json({ count: row.count });
  }

  if (req.method === "GET") {
    const rows = await db.select().from(pageViews).where(eq(pageViews.path, SITE_KEY));
    return Response.json({ count: rows[0]?.count ?? 0 });
  }

  return new Response("Method not allowed", { status: 405 });
};

export const config: Config = {
  path: "/api/views",
};
