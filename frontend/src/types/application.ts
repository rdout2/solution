// src/types/application.ts

export type ApplicationStatus = 'Wishlist' | 'Applied' | 'Interview' | 'Offer' | 'Rejected';

export interface Application {
  id: number;
  title: string;
  company: string;
  status: ApplicationStatus;
  date_applied: string | null;
  job_board?: string | null;
  location?: string | null;
  notes?: string | null;
  created_at: string;
  logo?: string;
}


export interface GroupedApplications {
  Wishlist: Application[];
  Applied: Application[];
  Interview: Application[];
  Offer: Application[];
  Rejected: Application[];
}
