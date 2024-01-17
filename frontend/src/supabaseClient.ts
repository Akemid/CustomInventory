import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
    'https://rjhqcugfyzmjwuikwjbw.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJqaHFjdWdmeXptand1aWt3amJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDM4MDUwOTIsImV4cCI6MjAxOTM4MTA5Mn0.5uYKNNZqovPWAhRW5zTRCgPX3ULTW3Aj91iUqxVhA4I'
    )