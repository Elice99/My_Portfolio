import { integer, pgTable, serial, text, timestamp } from "drizzle-orm/pg-core";

export const guestbookEntries = pgTable("guestbook_entries", {
  id: serial().primaryKey(),
  name: text().notNull(),
  message: text().notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const pageViews = pgTable("page_views", {
  path: text().primaryKey(),
  count: integer().notNull().default(0),
});
