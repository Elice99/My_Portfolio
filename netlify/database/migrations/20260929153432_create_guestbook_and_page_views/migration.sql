CREATE TABLE "guestbook_entries" (
	"id" serial PRIMARY KEY,
	"name" text NOT NULL,
	"message" text NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "page_views" (
	"path" text PRIMARY KEY,
	"count" integer DEFAULT 0 NOT NULL
);
