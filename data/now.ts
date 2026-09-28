export interface NowItem {
  status: "BUILDING" | "DEVELOPING" | "EXPLORING" | "LEARNING";
  title: string;
  subtitle: string;
  verified: boolean;
}

export const nowItems: NowItem[] = [
  {
    status: "BUILDING",
    title: "TrustLake",
    subtitle: "Data Trust Engine — pre-MVP, backend foundation stage",
    verified: true,
  },
  {
    status: "DEVELOPING",
    title: "Market Research @ Dechsoft",
    subtitle: "Quantitative business-audience research track",
    verified: true,
  },
  {
    status: "EXPLORING",
    title: "AdminOps",
    subtitle: "AI × Business Operations",
    // Named in Elice's own wireframe spec but not yet detailed elsewhere —
    // replace/remove if this isn't active.
    verified: false,
  },
  {
    status: "EXPLORING",
    title: "Geospatial Analytics",
    subtitle: "Earth Science × Data",
    verified: false,
  },
];
